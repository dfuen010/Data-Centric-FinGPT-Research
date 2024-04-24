const tipranksApi = require('tipranks-api-v2');
tipranksApi.getPriceTargets('TSLA').then(result => console.log(result));
tipranksApi.getNewsSentimentData('TSLA').then(result => console.log(result));
tipranksApi.getTrendingStocks().then(trending => console.log(trending));

