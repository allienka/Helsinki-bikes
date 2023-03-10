var express = require('express');
var router = express.Router();
var database = require('../database');
var {PythonShell} =require('python-shell');

var options={
    
    mode: 'text',
    pythonOptions: ['-u'], 
    scriptPath: '', 
    
};
router.get('/', function (req, res, next) {
    res.render('index', { title: 'Express' });
});

const { spawn } = require('child_process')
router.get('/', function(req, res) {
  
    const scriptPath = '../import/mainstations.py'
    const process = spawn('python', [scriptPath])
    process.stdout.on('data', (myData) => {
        
    })
    process.stderr.on('data', (myErr) => {
       
    })
});


PythonShell.run('../import/mainstations.py', options, function (err, result){
      if (err) throw err;
      
      console.log('Validations OK. Data inserted');
     
    });

router.get('/get_data', function (request, response, next) {

    var draw = request.query.draw;

    var start = request.query.start;

    var length = request.query.length;

    var order_data = request.query.order;

    if (typeof order_data == 'undefined') 
    {
        var column_name = 'hsl_stations.STATION_ID';

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
   AND (STATION LIKE '%${search_value}%' 
   
    )
  `;


    //Total number of records without filtering

    database.query("SELECT COUNT(*) AS Total FROM hsl_stations", function(error, data) {

        var total_records = data[0].Total;

        //Total number of records with filtering

        database.query(`SELECT COUNT(*) AS Total FROM hsl_stations WHERE 1 ${search_query}`, function (error, data) {

            var total_records_with_filter = data[0].Total;

            var query = `
          SELECT * FROM hsl_stations 
          WHERE 1 ${search_query} 
          ORDER BY ${column_name} ${column_sort_order} 
          LIMIT ${start}, ${length}
          `;

            var data_arr = [];

            database.query(query, function(error, data) {

                data.forEach(function (row) {
                    data_arr.push({
                        'STATION': row.STATION,
                        'ADDRESS':row.ADDRESS,
                        'JOURNEYS_STARTED': row.JOURNEYS_STARTED,
                        'JOURNEYS_ENDED': row.JOURNEYS_ENDED,
                        'AVG_STARTING_JOURNEY_DIST': row.AVG_STARTING_JOURNEY_DIST,
                        'AVG_ENDING_JOURNEY_DIST': row.AVG_ENDING_JOURNEY_DIST
                        
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
