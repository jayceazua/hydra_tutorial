# hydra_tutorial

## Hydra - Notes

#### Strict Mode:
 - accessing a key that is not in the config file will result in a KeyError instead of returning None
  
 - trying to insert a new key will result in a KeyError not add it.

 - strict mode is on by default. could be turned on and off

#### Config Groups:
   - most important concept of hydra
   - "suppose you benchmark" PostgreSQL and MySQL, you will need either but not both.

  - mutually exclusive set of config files.
  1. create a directory called 'db' that can hold a file for each database config alternatives
   - move all the config files into conf directory
  - after you can choose which database to config
  - you can compose your config object from multiple config files
 - config files that not a part of a config group like db cannot bee overriden


 #### vocab: 
  - parameter sweep
  - dimension you want to "sweep"
  - locally and serially
  

