import pandas as pd


def load_dataset(filepath):
    """Loading sample dataset or a specific dataset

    Parameters
    ----------
    filepath : str
      Filepath of sample dataset. If specified, file must match pattern of sample dataset.

    Returns
    -------
    gr : 1D numpy array, shape (n_samples,)
      The GR curve
    mud_volume : 1D numpy array, shape (n_samples,)
      The mud volume curve
    tvd : 1D numpy array, shape (n_samples,)
      The TVD curve
    """

    dataset = pd.read_csv(filepath)
    depth = dataset.Depth.values
    gr = dataset.GR.values
    mud_volume = dataset.MUD_VOLUME.values
    tvd = dataset.TVD.values
    biostrat = dataset.Biostratigraphy.values
    relia = dataset.Reliability.values
    core_depo = dataset.Core_depofacies.values
    lateral = dataset.Lateral_proximity.values
    special_litho = dataset.Special_lithology.values

    return {
        "Depth": depth,
        "GR": gr,
        "MUD_VOLUME": mud_volume,
        "TVD": tvd,
        "Biostratigraphy": biostrat,
        "Reliability": relia,
        "Core_depofacies": core_depo,
        "Lateral_proximity": lateral,
        "Special_lithology": special_litho
    }
