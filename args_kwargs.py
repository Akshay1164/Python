def log_metrics(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

log_metrics("accuracy","f1",model="xgboost", epochs=10, learning_rate=0.01)
