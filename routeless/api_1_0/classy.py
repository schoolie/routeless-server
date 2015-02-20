# Embedded file name: C:\Development\routeless-server\routeless\api_1_0\classy.py
from flask.ext.classy import FlaskView
quotes = ['A noble spirit embiggens the smallest man! ~ Jebediah Springfield', 'If there is a way to do it better... find it. ~ Thomas Edison', 'No one knows what he can do till he tries. ~ Publilius Syrus']

class QuotesView(FlaskView):

    def index(self):
        return '<br>'.join(quotes)

    def get(self, id):
        return '<p>%s</p>' % quotes[int(id)]