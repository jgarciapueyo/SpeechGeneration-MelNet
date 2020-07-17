"""
This module contains classes to log the training process as well as save the logs in a Tensorboard
format.
"""
from torch.utils.tensorboard import SummaryWriter

from src.utils.hparams import HParams


class TensorboardWriter:
    """
    Writes logs to be visualized in Tensorboard
    """

    def __init__(self, hp: HParams):
        """
        Args:
            hp (HParams): parameters for logging. Parameters used are hp.logging.dir_log_tensorboard
        """
        self.writer = SummaryWriter(log_dir=hp.logging.dir_log_tensorboard)

    def log_training(self, loss: int, epoch: int):
        """
        Logging information related to training.

        Args:
            loss (int): loss during training
        """
        self.writer.add_scalar(tag='train/loss', scalar_value=loss, global_step=epoch)

    def log_end_training(self, hp: HParams, loss: int):
        """
        Logging parameters of the training and final loss.

        Args:
            hp:
            loss:
        """
        params = get_important_hparams(hp)
        metrics = {'loss': loss}
        self.writer.add_hparams(hparam_dict=params, metric_dict=metrics)


def get_important_hparams(hp: HParams) -> dict:
    """
    Get the important params for training to store them in tensorboard logs
    Args:
        hp (HParams): parameters

    Returns:
        important_params (dict)
    """
    important_params = dict()
    # dataset
    important_params["data.dataset"] = hp.data.dataset

    # audio
    important_params["audio.sample_rate"] = hp.audio.sample_rate
    important_params["audio.spectrogram_type"] = hp.audio.spectrogram_type
    important_params["audio.n_fft"] = hp.audio.n_fft
    important_params["audio.mel_channels"] = hp.audio.mel_channels
    important_params["audio.hop_length"] = hp.audio.hop_length
    important_params["audio.win_length"] = hp.audio.win_length
    important_params["audio.ref_level_db"] = hp.audio.ref_level_db
    important_params["audio.min_level_db"] = hp.audio.min_level_db

    # network
    important_params["network.n_tiers"] = hp.network.n_tiers
    important_params["network.layers"] = '_'.join(map(str, hp.network.layers))
    important_params["network.hidden_size"] = hp.network.hidden_size
    important_params["network.gmm_size"] = hp.network.gmm_size

    # training
    important_params["training.optimizer"] = hp.training.optimizer
    important_params["training.epochs"] = hp.training.epochs
    important_params["training.batch_size"] = hp.training.batch_size
    important_params["training.lr"] = hp.training.lr
    important_params["training.momentum"] = hp.training.momentum

    return important_params



