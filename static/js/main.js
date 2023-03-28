
$(document).ready(function(){


    // Populate data using ajax
    $.ajax({
        url: "http://127.0.0.1:8000/request_data/",
        type: "GET",
        success: function(resp) {
            console.log(resp)
            let data= resp.accounts
            document.getElementById("trading_table").innerHTML=""
            data.forEach(result=>{
                console.log(result.server_name)
                let js_datetime = new Date(`${result.market_watch_time}`);
                js_datetime=js_datetime.toString()
                document.getElementById("trading_table").innerHTML +=`
                    <tr>
                        <td>${result.server_name}</td>
                        <td>${result.equity}</td>
                        <td>${result.balance}</td>
                        <td>${js_datetime.slice(4,24)}</td>
                    </tr>

                    `

            })

            
        },
        error: function(err) {
           console.log(err)
        }
    });
    
    // Fetch data every 1mins
    function fetchAccount() {
        $.ajax({
            url: "http://127.0.0.1:8000/request_data/",
            type: "GET",
            success: function(resp) {
                console.log(resp)
                let data= resp.accounts
                document.getElementById("trading_table").innerHTML=""
                data.forEach(result=>{
                    console.log(result.server_name)
                    let js_datetime = new Date(`${result.market_watch_time}`);
                    js_datetime=js_datetime.toString()
                    document.getElementById("trading_table").innerHTML +=`
                        <tr>
                            <td>${result.server_name}</td>
                            <td>${result.equity}</td>
                            <td>${result.balance}</td>
                            <td>${js_datetime.slice(4,24)}</td>
                        </tr>

                        `

                })

                
            },
            error: function(err) {
               console.log(err)
            }
        });
    }
    
    $(document).ready(function() {
        setInterval(fetchAccount, 60000); // call the function every minute (60,000 milliseconds)
    });
    
});

