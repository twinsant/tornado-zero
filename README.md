# Tornado project code base

With jQuery, Bootstrap and Backbone.js


    mkdir /your/project
    git archive zero|tar -x -C /your/project

    mkvirtualenv --python=python2.7 --no-site-pacakges --distribute codename
    pip install -r requirements.txt

    cp local_conf.py.sample local_conf.py
    python main.py --debug
