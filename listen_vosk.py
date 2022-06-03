import json
import queue
import sounddevice as sd
import sys
import time
import vosk

vosk.SetLogLevel(-1)

__model = vosk.Model(lang="en-us")
__device = None
__device_info = sd.query_devices(__device, 'input')
__samplerate = int(__device_info['default_samplerate'])

def listen(timeout=10):
    def callback(indata, frames, time, status):
        if status:
            print(status, file=sys.stderr)
        q.put(bytes(indata))

    q = queue.Queue()

    with sd.RawInputStream(samplerate=__samplerate, blocksize = 8000, device=__device, dtype='int16', channels=1, callback=callback):
        rec = vosk.KaldiRecognizer(__model, __samplerate)
        start = time.time()
        res_json = '{"text":""}'
        while True:
            data = q.get(timeout=timeout)
            if data is None:
                break
            if rec.AcceptWaveform(data):
                res_json = rec.Result()
                break
            elif time.time() - start > timeout:
                res_json = rec.PartialResult()
                break
        res = json.loads(res_json)
        is_complete = 'text' in res
        text = res['text'] if is_complete else res['partial']
        return (text, is_complete)
