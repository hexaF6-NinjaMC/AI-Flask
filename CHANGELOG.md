* __24w37a / 2024-09-12:__ 
  * Utilized application through __`https://ai-flask-production.up.railway.app/`__.
    > Please remain aware this may change back to `https://ai-flask-m190.onrender.com/`. This may also be featured through a registered __*\(sub-\)*__ domain.

  * Updated Python version to __*`3.12.6`*__, and updated package dependencies to latest supported versions. Check `requirements.txt` for details.

  * Changed NLTK configuration to use the __`punkt_tab`__ data.

  * Changed
      ```python
      torch.load(file, weights_only=True)
      ```
    to use
      ```python
      weights_only=True
      ```
    which will be enabled by default in later versions of `torch`.

  * Updated '/upload' route to include the
      ```html
      <a href="/logout">Logout</a>
      ```
    feature from the `base.html`, as this is the only authenticated route served.

  * Resolved a typo in the `chatbot_index()` function docstring.

  * Updated REST file to utilize Render and localhost URLs.
    > May add Railway (and, if utilized, the custom domain) URLs.

  * Styled register, login, and upload pages with a dark-mode theme.

  * Committed the updated `intents.json` training data.

  * Added the __`CHANGELOG.md`__.
