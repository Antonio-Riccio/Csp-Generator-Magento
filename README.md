CspGeneretor (unofficial Script)
======

![Tux, the Linux mascot](https://www.evemilano.com/wp-content/uploads/2017/06/Magento_logo.png)

This script allows you to generate magento CSP module with few simple clicks.
Form creation is completely dynamic.
The module version, name, report type, and soon also the policy value id.
The id can be of two types incremental, from 0 to X or by hostname, ex id=cloudflare host=cloudflare.com

In the script there is already a default host list but using a log file you can also generate a custom host list which will be inserted in the csp_whitelist.xml file. (the script automatically recognizes the type CSP Code)

The default list will be updated over time to simplify module creation

# Help
Usage: CspGeneretor.py [-h] [--nameModule NAMEMODULE] [--fileLog FILELOG] [--version VERSION] [--setId SETID]
               [--trt TRT] [--tra TRA]


options:

  -h, --help            show this help message and exit
  
  --nameModule          Name Module CSP
  
  --fileLog FILELOG     Path file Log
  
  --version VERSION     Version Module
  
  --setId SETID         Id value (for the moment it is only numerical)
  
  --trt TRT             Type report storefront
  
  --tra TRA             Type report admin

  # Step 1
  Using DevTool for save log or using default whitelist (Right click on log in console and save file)

  # Step 2
  Run the script and insert
  1. Name Module --nameModule
  2. Add log file name --fileLog (if needed)
  3. Add version --version (by default it is set to 1)
  4. Add type Id --setId (0=number 1=name Host for the moment it is only numerical)
  5. Add value for type report storefront --trt (0 or 1)
  6. Add value for type report admin --tra (0 or 1)
  
  # Step 3 
  1. Import Module On Project 
  2. Run `php bin/magento setup:upgrade`, `php bin/magento setup:di:compile` and `php bin/magento cache:flush`
  3. Good job

---------------------------

# Info

# Type CSP Code
- default-src -> The default policy. 

- style-src -> Defines the sources for stylesheets. 

- font-src -> Defines which sources can serve fonts.

- object-src -> Defines the sources for the ,, and elements.

- script-src -> Defines the sources for JavaScript elements.

- img-src	-> Defines the sources from which images can be loaded.

- form-action -> Defines valid endpoints for submission from tags.

- media-src -> Defines the sources from which images can be loaded.

- manifest-src -> Defines the allowable contents of web app manifests.

- base-url -> Defines which URLs can appear in a page’s <base> element.

- frame-ancestors -> Defines the sources that can embed the current page.

- child-src	-> Defines the sources for workers and embedded frame contents.

- connect-src	-> Defines the sources that can be loaded using script interfaces.

---------------------------

# Type Content Security Policy:

- report only – Magento reports the policy violations but does not act upon it. It is mainly used for debugging. CSP works in this mode by default.

- restrict mode – Magento acts in the case of policy violations.

---------------------------

# Status Script

### Type CSP Code
## Work

- script-src
- style-src
- font-src
- frame-ancestors
- connect-src
- img-src

## Not Work

- default-Src 
- base-Url 
- child-Src 
- form-action 	
- manifest-src 
- media-src 
- object-src 

### Discoverable Domains
## Work

- .it
- .com

## Not Work (More domains will be added in the coming days)
- All the others
