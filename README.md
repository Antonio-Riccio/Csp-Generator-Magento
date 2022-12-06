# Csp-Generetor-Magento
this script allows you to automatically generate a csp_whitelist.xml file

Giude:
  # Step 1
  Using DevTool for save log or using default whitelist

  # Step 2
  Run the script and insert
  1. Name Module 
  2. Set Report only or Restrict mode 
  3. Path file log saved in the step 1 / nothing if you chose using default whitelist

  # Step 3 
  1. Import folder generated 
  2. apply database updates by running `php bin/magento setup:upgrade`
  3. Flush the cache by running `php bin/magento cache:flush`
  4. Good job

___

# Info

- # Type CSP Code
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

___
- # Set CSP Works

- report – only – Magento reports the policy violations but does not act upon it. It is mainly used for debugging. CSP works in this mode by default.

- restrict mode – Magento acts in the case of policy violations.

___
# Status

# Type CSP Code
- # Work
- script-src
- style-src
- font-src
- frame-ancestors
- connect-src
- img-src

- # Not Work
- default-Src 
- base-Url 
- child-Src 
- form-action 	
- manifest-src 
- media-src 
- object-src 

# Discoverable Domains
- # Work
- it
- com

- # Not Work (More domains will be added in the coming days)
- All the others

