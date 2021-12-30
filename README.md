# 3D Print Matcher

Hackathon winning project 🏅 that consisted in identifying what `.stl` file was 3d printed based on a image of the printed pice. The picture shouble be able to be taken from the phone and we get the list of possible `.stl` files.

**The full project explanation is in the [DevPost project's page](https://devpost.com/software/identificador-de-impressions-3d-per-imatge).**

## Develop

This is a monorepo where every system is in a folder.

To run: Run the `matcher-client` and `matcher-server`, and open the client with chrome with CORSS disabled.

```sh
open -na "Google Chrome" --args --user-data-dir=/tmp/temp_chrome_user_data_dir http://localhost:8080/ --disable-web-security
```
