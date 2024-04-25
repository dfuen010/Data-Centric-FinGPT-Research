const tipranksApi = require('tipranks-api-v2');

tipranksApi.getPriceTargets('TSLA').then(result => console.log(result));
tipranksApi.getNewsSentimentData('TSLA').then(result => console.log(result));
tipranksApi.getTrendingStocks().then(trending => console.log(trending));

//supposed to return the following

// {
//   "symbol": "TSLA",
//   "priceTargets": {
//     "mean": 297.3333333333333,
//     "median": 300,
//     "highest": 500,
//     "lowest": 54,
//     "numberOfEstimates": 21
//   }
// }

// {
//   "symbol": "TSLA",
//   "sentiment": {
//     "bullishPercent": 0.4062,
//     "bearishPercent": 0.5938
//   },
//   "buzz": {
//     "articlesInLastWeek": 143,
//     "weeklyAverage": 147.25,
//     "buzz": 0.9711
//   },
//   "sectorAverageBullishPercent": 0.6204,
//   "sectorAverageNewsScore": 0.52,
//   "companyNewsScore": 0.3969
// }

// [
//   {
//     "ticker": "HAL",
//     "popularity": 10,
//     "sentiment": 10,
//     "consensusScore": 1,
//     "operations": null,
//     "sector": "BASIC MATERIALS",
//     "sectorID": 17343,
//     "marketCap": 18394572000,
//     "buy": 10,
//     "sell": 0,
//     "hold": 0,
//     "priceTarget": 32.42,
//     "rating": 5,
//     "companyName": "Halliburton",
//     "quarterlyTrend": 5,
//     "lastRatingDate": "2019-07-24T00:00:00"
//   },
//   {
//     "ticker": "XLNX",
//     "popularity": 9,
//     "sentiment": 6,
//     "consensusScore": 1.6666666666666667,
//     "operations": null,
//     "sector": "CONSUMER GOODS",
//     "sectorID": 18731,
//     "marketCap": 27832018900,
//     "buy": 6,
//     "sell": 0,
//     "hold": 3,
//     "priceTarget": 131.6,
//     "rating": 4,
//     "companyName": "Xilinx Inc",
//     "quarterlyTrend": 4,
//     "lastRatingDate": "2019-07-26T00:00:00"
//   }
// ]