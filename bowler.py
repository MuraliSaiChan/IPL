import scrapy


class BowlerSpider(scrapy.Spider):
    name = 'bowler'
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
            # result = item.xpath(".//div[@class='cb-col cb-scrcrd-status cb-col-100 cb-text-complete']/text()").get()
            link = "https://www.cricbuzz.com"+item.xpath(".//@href").get().replace("cricket-scores",'live-cricket-scorecard')
            # req = scrapy.Request()
            yield response.follow(link,self.data, meta={'match':match,'season':season})
            #//div[@class="cb-col cb-scrcrd-status cb-col-100 cb-text-complete ng-scope"]/text()
            
    def data(self, response):
        season = response.meta['season']
        match = response.meta['match']
        result = response.xpath("//div[@class='cb-col cb-scrcrd-status cb-col-100 cb-text-complete']/text()").get()
        #innings1
        bowler = response.xpath("//div[@id='innings_1']/div[@class='cb-col cb-col-100 cb-ltst-wgt-hdr'][2]/div[@class='cb-col cb-col-100 cb-scrd-itms ']")
        team = response.xpath("//div[@id='innings_2']/div[@class='cb-col cb-col-100 cb-ltst-wgt-hdr'][1]/div[1]/span/text()").get()
        for i in bowler[:-2]:
            name = i.xpath(".//div[1]/a/text()").get()
            overs = i.xpath(".//div[2]/text()").get()
            maidens = i.xpath(".//div[3]/text()").get()
            runs = i.xpath(".//div[4]/text()").get()
            wickets = i.xpath(".//div[5]/text()").get()
            noballs = i.xpath(".//div[6]/text()").get()
            wides = i.xpath(".//div[7]/text()").get()
            eco = i.xpath(".//div[8]/text()").get()
            # if name != '':
            yield {
                'season':season,
                'match': match,
                'result':result,
                'team':team,
                'innings':'2nd innings',
                'bowler_name': name,
                'overs':overs,
                'maidens':maidens,
                'runs':runs,
                'wickets':wickets,
                'noballs':noballs,
                'wides': wides,
                'economy':eco
                }
        #innings2
        bowler = response.xpath("//div[@id='innings_2']/div[@class='cb-col cb-col-100 cb-ltst-wgt-hdr'][2]/div[@class='cb-col cb-col-100 cb-scrd-itms ']")
        team = response.xpath("//div[@id='innings_1']/div[@class='cb-col cb-col-100 cb-ltst-wgt-hdr'][1]/div[1]/span/text()").get()
        for i in bowler[:-2]:
            name = i.xpath(".//div[1]/a/text()").get()
            overs = i.xpath(".//div[2]/text()").get()
            maidens = i.xpath(".//div[3]/text()").get()
            runs = i.xpath(".//div[4]/text()").get()
            wickets = i.xpath(".//div[5]/text()").get()
            noballs = i.xpath(".//div[6]/text()").get()
            wides = i.xpath(".//div[7]/text()").get()
            eco = i.xpath(".//div[8]/text()").get()
            # if name != '':
            yield {
                'season':season,
                'match': match,
                'result':result,
                'team':team,
                'innings':'2nd innings',
                'bowler_name': name,
                'overs':overs,
                'maidens':maidens,
                'runs':runs,
                'wickets':wickets,
                'noballs':noballs,
                'wides': wides,
                'economy':eco
                }

