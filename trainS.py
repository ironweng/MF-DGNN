from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import yaml
from base_functions import MFTDGNNSupervisor
import torch

def main(args):
    with open(args.config_filename) as f:
        supervisor_config = yaml.load(f,Loader=yaml.FullLoader)
        torch.cuda.empty_cache()
        supervisor = MFTDGNNSupervisor(**supervisor_config)
        supervisor.trainS()



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--config_filename', default='data/parameters/electricity.yaml', type=str,
                        help='Configuration filename for restoring the model.')
    args = parser.parse_args()
    main(args)

