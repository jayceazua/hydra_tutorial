import hydra

@hydra.main(config_path='conf/config.yaml')
def my_app(cfg):
  """
    cfg is an OmegaConfig object that holds the config for your function.

  """
  print(cfg.pretty())

if __name__ == "__main__":
  my_app()


