# RipperWare

RipperWare is the user interface running on Razza's CD Ripper. It's written in Python and leverages PyGame to render the user interface.

If you're looking to build your own, [check out the project page][project-page]. Updates and docs will be published to [this website][project-hub].

> Right now, the repo and CI is set up to make it easier to iterate and push the software to my own Ripper running it. If this somehow gets wider option, I will split it up into a "stable" and "wip" branches.

[project-page]: https://razza.io/projects/ripper.html
[project-hub]: https://ripper.razza.io/

## Wishlist

- [ ] Rip CD-ROM and DVD-ROM ([dd], what else?)
- [ ] Rip Audio CD ([cdparanoia])
    - [ ] add support for CD-Text
- [ ] Burn "Yellow Book" CD-R and DVD-R/DVD+R
- [ ] Burn "Red Book" CD-R
    - [ ] with support for CD-Text
- [ ] Refactor the UI library into its own project

[dd]: https://manpages.debian.org/bookworm/coreutils/dd.1.en.html
[cdparanoia]: https://xiph.org/paranoia/

## Running it

Running it will pretty much be a variation of: create venv, install deps, run it in venv.

### Production Mode

By default, the application runs in "test mode", where given "work units" get stubbed by a fake one, so requesting to rip/burn a disc will no call out to external dependencies.

To disable this "test mode", set the `RIPPERWARE_ENV` envvar to `prod`. The Debian package script will do this for release artifacts.

## Building it

On a system with Debian packaging tools installed, run `debian/mkdeb.sh`. It will drop the resulting `.deb` in `debian/out` folder.
