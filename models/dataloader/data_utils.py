from common.utils import set_seed


def dataset_builder(args):  # download dataset files
    set_seed(args.seed)  # fix random seed for reproducibility

    if args.dataset == 'miniimagenet':
        from models.dataloader.mini_imagenet import MiniImageNet as Dataset
    elif args.dataset == 'cars':
        from models.dataloader.cars import Cars as Dataset
    elif args.dataset == 'cub_crop':
        from models.dataloader.cub_crop import cub_crop as Dataset    
    elif args.dataset == 'Aircraft_fewshot':
        from models.dataloader.aircarft import Aircarft as Dataset
    else:
        raise ValueError('Unkown Dataset')
    return Dataset
