# Classviz-Tool
## Implementation progress:
- [ ] Robustness (e.g. when user input a non-JSON file)
- [ ] Download the input JSON file from Galaxy to classviz/data folder
- [ ] Add script to load input json file when opening classviz

## Set up:
1. Setup Galaxy as mentioned in [AST-Creation-Tool README.md](https://github.com/Moonshot-SEP/AST-Creation-Tool/blob/main/README.md)
2. Go to the directory `galaxy/tools/moonshot/` and clone this repository
3. Change the galaxy tool configuration at `config/tool_conf.xml.sample` by adding:
   ```<section name="Moonshot" id="moonshot">
        <tool file="moonshot/AST-Creation-Tool/zip_to_spif.xml" />
        <tool file="moonshot/Classviz-Tool/classviz.xml" />
      </section>
   ```
## How to use the tool:
1. Build and run Galaxy as normal.
2. Navigate on the left `Tools column > Moonshot > Classviz`.
3. Upload a JSON file.
4. Click on "Run Tool".
5. Copy the display link (http://127.0.0.42:7800/) and open it in another browser.
