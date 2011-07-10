from pyramid.config import Configurator
from paste.httpserver import serve
from pyramid.session import UnencryptedCookieSessionFactoryConfig

if __name__ == '__main__':
    my_session_factory = UnencryptedCookieSessionFactoryConfig('itsaseekreet')
    config = Configurator(session_factory=my_session_factory)
    config.add_route('session_test', '/session_test')
    config.scan('views')
    serve(config.make_wsgi_app())
    
