from src.validate.profiling import (
    run_profiling_pipeline
)

from src.pipeline.consolidation_pipeline import (
    run_consolidation_pipeline
)


if __name__ == "__main__":

    run_profiling_pipeline()

    run_consolidation_pipeline()