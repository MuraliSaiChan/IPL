import scrapy

#spider_name : spider1
class Spider1Spider(scrapy.Spider):
    name = 'spider1'
    allowed_domains = ['www.cricbuzz.com']
    start_urls = ['https://www.cricbuzz.com/cricket-series/2058/indian-premier-league-2008/matches',
                  'https://www.cricbuzz.com/cricket-series/2059/indian-premier-league-2009/matches',
                  'https://www.cricbuzz.com/cricket-series/2060/indian-premier-league-2010/matches',
                  'https://www.cricbuzz.com/cricket-series/2037/indian-premier-league-2011/matches',
                  'https://www.cricbuzz.com/cricket-series/2115/indian-premier-league-2012/matches',
                  'https://www.cricbuzz.com/cricket-series/2170/indian-premier-league-2013/matches',
                  'https://www.cricbuzz.com/cricket-series/2261/indian-premier-league-2014/matches',
                  'https://www.cricbuzz.com/cricket-series/2330/indian-premier-league-2015/matches',
                  'https://www.cricbuzz.com/cricket-series/2430/indian-premier-league-2016/matches',
                  'https://www.cricbuzz.com/cricket-series/2568/indian-premier-league-2017/matches',
                  'https://www.cricbuzz.com/cricket-series/2676/indian-premier-league-2018/matches',
                  'https://www.cricbuzz.com/cricket-series/2810/indian-premier-league-2019/matches',
                  'https://www.cricbuzz.com/cricket-series/3130/indian-premier-league-2020/matches',
                  'https://www.cricbuzz.com/cricket-series/3472/indian-premier-league-2021/matches',
                  'https://www.cricbuzz.com/cricket-series/4061/indian-premier-league-2022/matches']

    def parse(self, response):
        season = response.xpath('//div[@class="cb-col-100 cb-col cb-nav-main cb-bg-white"]/h1/text()').get()
        for item in response.xpath("//a[@class='text-hvr-underline']"):
            match = item.xpath('.//text()').get()
            link = "https://www.cricbuzz.com"+item.xpath(".//@href").get().replace("cricket-scores",'live-cricket-scorecard')
            # req = scrapy.Request()
            yield response.follow(link,self.data, meta={'match':match,'season':season})
            #//div[@class="cb-col cb-scrcrd-status cb-col-100 cb-text-complete ng-scope"]/text()
            
    def data(self, response):
        season = response.meta['season']
        match = response.meta['match']
        #innings1
        batter = response.xpath("//div[@id='innings_1']/div[@class='cb-col cb-col-100 cb-ltst-wgt-hdr'][1]/div[@class='cb-col cb-col-100 cb-scrd-itms']")
        team = response.xpath("//div[@id='innings_1']/div[@class='cb-col cb-col-100 cb-ltst-wgt-hdr'][1]/div[1]/span/text()").get()
        for i in batter[:-2]:
            name = i.xpath(".//div[1]/a/text()").get()
            out = i.xpath(".//div[2]/span/text()").get()
            runs = i.xpath(".//div[3]/text()").get()
            balls = i.xpath(".//div[4]/text()").get()
            fours = i.xpath(".//div[5]/text()").get()
            sixes = i.xpath(".//div[6]/text()").get()
            srate = i.xpath(".//div[7]/text()").get()
            if name != '':
                yield {
                    'season':season,
                    'match': match,
                    'team':team,
                    'innings':'1st innings',
                    'batter_name': name,
                    'out_style': out,
                    'runs':runs,
                    'balls':balls,
                    'fours':fours,
                    'sixes':sixes,
                    'strike rate':srate
                    }
        #innings2
        batter = response.xpath("//div[@id='innings_2']/div[@class='cb-col cb-col-100 cb-ltst-wgt-hdr'][1]/div[@class='cb-col cb-col-100 cb-scrd-itms']")
        team = response.xpath("//div[@id='innings_2']/div[@class='cb-col cb-col-100 cb-ltst-wgt-hdr'][1]/div[1]/span/text()").get()
        for i in batter[:-2]:
            name = i.xpath(".//div[1]/a/text()").get()
            out = i.xpath(".//div[2]/span/text()").get()
            runs = i.xpath(".//div[3]/text()").get()
            balls = i.xpath(".//div[4]/text()").get()
            fours = i.xpath(".//div[5]/text()").get()
            sixes = i.xpath(".//div[6]/text()").get()
            srate = i.xpath(".//div[7]/text()").get()
            if name != '':
                yield {
                    'season':season,
                    'match': match,
                    'team':team,
                    'innings':'2nd innings',
                    'batter_name': name,
                    'out_style': out,
                    'runs':runs,
                    'balls':balls,
                    'fours':fours,
                    'sixes':sixes,
                    'strike rate':srate
                    } 
