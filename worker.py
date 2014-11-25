@gen.coroutine
def main():
    # do stuff...

if __name__ == '__main__':
    IOLoop.instance().run_sync(main)