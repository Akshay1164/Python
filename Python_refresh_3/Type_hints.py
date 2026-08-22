from typing import List, Dict, Optional

def predict_batch(inputs: List[float], threshold: Optional[float] = 0.5) -> Dict[str,float]:
    return {"prediction": sum(inputs)/len(inputs), "threshold": threshold}

def predict_batch2(inputs: List[float], threshold: Optional[float] = 0.5) -> Dict[str,float]:
    if not inputs:
        return {"prediction": 0.0, "threshold": threshold}
    return {"prediction": sum(inputs)/len(inputs), "threshold": threshold}

print(predict_batch([1,2,3,4,5]))
print(predict_batch2([1,2,3,4,5]))
print(predict_batch2([]))