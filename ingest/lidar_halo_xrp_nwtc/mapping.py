import re

from typing import AnyStr, Dict
from utils import IngestSpec, expand
from . import LidarHaloXrpPipeline


mapping: Dict["AnyStr@compile", IngestSpec] = {
    # Mapping for Raw Data -> Ingest
    re.compile(r".*Stare_199_\d{8}_\d{2}\.hpl"): IngestSpec(
        pipeline=LidarHaloXrpPipeline,
        pipeline_config=expand("config/pipeline_config_nwtc.yml", __file__),
        storage_config=expand("config/storage_config.yml", __file__),
        name="awaken_buoy_ingest",
    ),
    # Mapping for Processed Data -> Ingest (so we can reprocess plots)
    re.compile(r".*nwtc\.lidar-halo_xrp\.b0\.\d{8}\.\d{6}\.nc"): IngestSpec(
        pipeline=LidarHaloXrpPipeline,
        pipeline_config=expand("config/pipeline_config_nwtc.yml", __file__),
        storage_config=expand("config/storage_config.yml", __file__),
        name="plot_awaken_buoy_ingest",
    ),
}
