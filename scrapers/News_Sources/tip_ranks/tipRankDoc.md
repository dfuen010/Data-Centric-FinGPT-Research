## Documentation for Tip Ranks Github API

### Installation


        npm init      - to scaffold the Node.js project

        npm install tipranks-api-v
    
### Usage
    
    const tipranksApi = require('tipranks-api-v2');

    // Get Price Targets for Specified Company
    tipranksApi.getPriceTargets('MU').then(result => console.log(result));

    // Get News Sentiment for Specified Company
    tipranksApi.getNewsSentimentData('MU').then(result => console.log(result));

    // Outputs Latest Trending Stocks, No Company Needed to Specify
    tipranksApi.getTrendingStocks().then(trending => console.log(trending));

    ^^ Latest Trending Stocks listed on website tipranks



##### Please Note:
The code in the tip_ranks folder doesn't have the required modules because it would be too many files in the repo. Only the js and resulting json file are located on the repository. Therefore you must run the installation to get the required node_modules and packages to run the code in the tip_ranks folder.


##### Here is the TipRanks API Repository:
https://github.com/janlukasschroeder/tipranks-api-v2








