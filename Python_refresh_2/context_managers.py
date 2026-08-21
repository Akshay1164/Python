class ModelSession:
    def __enter__(self):
        print("Loading model...")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing model session...")


with ModelSession() as session:
    print("Model is ready to use.")

    