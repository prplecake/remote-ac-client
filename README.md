# remote-ac-client

This is the client portion of the [remote-ac-controller].

[remote-ac-controller]:https://github.com/prplecake/remote-ac-controller

## quickstart

requirements:

- [lirc](https://www.lirc.org/)

```shell
# setup pipenv and install packages
pipenv install
# start development server
honcho start
```

This gets the web interface set up along with the DHT sensor. Learn how to set
up lirc [on the wiki][lirc-wiki].

[lirc-wiki]: https://github.com/prplecake/remote-ac-homeserver/wiki/lirc

## see also

- [circuit schematic](https://github.com/prplecake/remote-ac-homeserver/wiki/Schematic)
- [frigidaire ac remote lirc config](https://gist.github.com/prplecake/71c4bc8584541cf7423b922b81733c3a)
- [IRreceiver MCU code](https://github.com/prplecake/IRreceiver)
