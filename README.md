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

Transformations are configured in [pretransform.txt](transformers/pretransform.txt) and
 [postransform.txt](transformers/posttransform.txt)
 
 Currently available transformation methods:
  - `Replace(target,replacemnet)`
  
# Rules

Rules are configured in [rulebook.txt](converter/rulebook.txt)
 
Currently available conversion commands:
  - `Ignore()`
  - `Strip()`
  - `Wrap(prefix, suffix [, allow_empty])`
  - `WrapIn(prefix, suffix, allow_empty, tag_list)`
  - `WrapOut(prefix, suffix, allow_empty, tag_list)`
  - `WrapWithAttribute(prefix, suffix, attr_name, attr_prefix, attr_suffix)`
  - `Config(config_name, value)`
  - `Table(prefix, suffix)`

For details please check the [rulebook.txt](converter/rulebook.txt) file
  