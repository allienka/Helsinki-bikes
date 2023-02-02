var express = require('express');
var router = express.Router();
var database = require('../database');

/* GET home page. */
router.get('/', function (req, res, next) {
    res.render('index', { title: 'Express' });
});
router.get('/get_data', function (request, response, next) {

    var draw = request.query.draw;

    var start = request.query.start;

    var length = request.query.length;

    var order_data = request.query.order;

    if (typeof order_data == 'undefined') 
    {
        var column_name = 'hsl_journeys.JOURNEYS_ID';

        var column_sort_order = 'desc';
    }
    else {
        var column_index = request.query.order[0]['column'];

        var column_name = request.query.columns[column_index]['data'];

        var column_sort_order = request.query.order[0]['dir'];
    }

    //search data

    var search_value = request.query.search['value'];

    var search_query = `
   AND (DEPARTURE_STATION LIKE '%${search_value}%' 
    OR RETURN_STATION LIKE '%${search_value}%' 
    OR DISTANCE LIKE '%${search_value}%' 
    OR DURATION LIKE '%${search_value}%'
   )
  `;

    //Total number of records without filtering

    database.query("SELECT COUNT(*) AS Total FROM hsl_journeys", function(error, data) {

        var total_records = data[0].Total;

        //Total number of records with filtering

        database.query(`SELECT COUNT(*) AS Total FROM hsl_journeys WHERE 1 ${search_query}`, function (error, data) {

            var total_records_with_filter = data[0].Total;

            var query = `
          SELECT * FROM hsl_journeys 
          WHERE 1 ${search_query} 
          ORDER BY ${column_name} ${column_sort_order} 
          LIMIT ${start}, ${length}
          `;

            var data_arr = [];

            database.query(query, function(error, data) {

                data.forEach(function (row) {
                    data_arr.push({
                        'DEPARTURE_STATION': row.DEPARTURE_STATION,
                        'RETURN_STATION': row.RETURN_STATION,
                        'DISTANCE': row.DISTANCE,
                        'DURATION': row.DURATION
                    });
                });

                var output = {
                    'draw': draw,
                    'iTotalRecords': total_records,
                    'iTotalDisplayRecords': total_records_with_filter,
                    'aaData': data_arr
                };

                response.json(output);

            });

        });

    });

});

module.exports = router;
