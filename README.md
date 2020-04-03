![PyTest](https://github.com/IstvanOri/HTML2MD/workflows/PyTest/badge.svg)

# HTML2MD
Configurable HTML to MarkDown converter

There are planty of converters from HTML to MD, but there are a lot of custom HTML tags and MarkDown dialects.
 So that this project aims to provide a configurable converter, in which the conversion rules can be altered.

I also use this project to learn Python :)

# Mechanism

 1. Read input
 1. Transform input by simple transformations (e.g. string replace)
 1. Process HTML and translate to MD 
 1. Transform output by simple transformations
 1. Write result
 
# Transformations

Transformations are configured in [pretransform.txt](data/pretransform.txt) and
 [postransform.txt](data/posttransform.txt)
 
 Currently available transformation methods:
  - `LinkFixer()`
  - `Replace(target,replacemnet)`
  - `RemoveWhiteSpace()`
  
# Rules

Rules are configured in [rulebook.txt](data/rulebook.txt)
 
Currently available conversion commands:
  - `Config(config_name, value)`
  - `Ignore()`
  - `Indent(indentation_prefix)`
  - `Level(indentation_prefix)`
  - `Strip()`
  - `Table(prefix, suffix)`
  - `Wrap(prefix, suffix [, allow_empty])`
  - `WrapIn(prefix, suffix, allow_empty, tag_list)`
  - `WrapOut(prefix, suffix, allow_empty, tag_list)`
  - `WrapWithAttribute(prefix, suffix, attr_name, attr_prefix, attr_suffix)`

For details please check the [rulebook.txt](data/rulebook.txt) file
  
