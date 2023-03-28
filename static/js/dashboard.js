$(document).ready(function(){


  // Turn of account chart on click event.
  $("#close_acc1").click(function(){
    console.log("Hit account1")
    $("#chart_Acc1").css("display","block")
    $("#chart_Acc2").css("display","none")
    $("#chart_Acc3").css("display","none")
  })
  $("#close_acc2").click(function(){
    console.log("Hit account2")
    $("#chart_Acc1").css("display","none")
    $("#chart_Acc2").css("display","block")
    $("#chart_Acc3").css("display","none")
  })
  $("#close_acc3").click(function(){
    console.log("Hit account3")
    $("#chart_Acc1").css("display","none")
    $("#chart_Acc2").css("display","none")
    $("#chart_Acc3").css("display","block")
  })

    // Get account details for each of the accounts
    let chart1="";
    let chart2="";
    // let chart3=""
    // Function can keeps fetching data
    fetchAccounts()
    function fetchAccounts(){
        // Us ajax request to fetch the data of each of the account every 1 mins
        $.ajax({
            type:"GET",
            url:"http://127.0.0.1:8000/dashboard_fetchdata/",
            success:function(resp){
                console.log(resp)
                let account_1=resp.account1
                let account_2=resp.account2
                let account_3=resp.account3
                let acc_1_time=[]
                let acc_1_equity=[]
                let acc_1_balance=[]
                let acc_2_time=[]
                let acc_2_equity=[]
                let acc_2_balance=[]
                let acc_3_time=[]
                let acc_3_equity=[]
                let acc_3_balance=[]

                account_1.forEach(e => {
                    let js_datetime = new Date(`${e.market_watch_time}`);
                    js_datetime=js_datetime.toString()
                    acc_1_time.push((js_datetime.slice(4,24)))
                    acc_1_equity.push(e.equity)
                    acc_1_balance.push(e.balance)
                  });
                  account_2.forEach(e => {
                    // acc_2_time.push(e.market_watch_time)
                    let js_datetime = new Date(`${e.market_watch_time}`);
                    js_datetime=js_datetime.toString()
                    acc_2_time.push(js_datetime.slice(4,24))
                    acc_2_equity.push(e.equity)
                    acc_2_balance.push(e.balance)
                  });
                  account_3.forEach(e => {
                    // acc_3_time.push(e.market_watch_time)
                    let js_datetime = new Date(`${e.market_watch_time}`);
                    js_datetime=js_datetime.toString()
                    acc_3_time.push(js_datetime.slice(4,24))
                    acc_3_equity.push(e.equity)
                    acc_3_balance.push(e.balance)
                  });
                  console.log(acc_3_balance)
            //    Populate Acoount1
            function loadAccount1(){
                const data = {
                    labels: acc_1_time.map(e => e),
                    datasets: [
                      {
                        label: 'Equity',
                        data: acc_1_equity.map(e => e),
                        borderColor: 'red',
                        fill: false,
                      },
                      {
                        label: 'Balance',
                        data: acc_1_balance.map(e => e),
                        borderColor: 'blue',
                        fill: false,
                      },
                    ],
                  };
                
                  const config = {
                    type: 'line',
                    data,
                    options: {
                      scales: {
                        x: {
                          title: {
                            display: true,
                            text: 'Time',
                          },
                        },
                        y: {
                          title: {
                            display: true,
                            text: 'Equity and Balance',
                          },
                        },
                      },
                    },
                  };
                   
                   chart1 = new Chart(document.getElementById('chart_Acc1'), config);
                   
            }
            loadAccount1()
            // Populate Acoount2
            function loadAccount2(){
                const data = {
                    labels: acc_2_time.map(e => e),
                    datasets: [
                      {
                        label: 'Equity',
                        data: acc_2_equity.map(e => e),
                        borderColor: 'red',
                        fill: false,
                      },
                      {
                        label: 'Balance',
                        data: acc_2_balance.map(e => e),
                        borderColor: 'blue',
                        fill: false,
                      },
                    ],
                  };
                
                  const config = {
                    type: 'line',
                    data,
                    options: {
                      scales: {
                        x: {
                          title: {
                            display: true,
                            text: 'Time',
                          },
                        },
                        y: {
                          title: {
                            display: true,
                            text: 'Equity and Balance',
                          },
                        },
                      },
                    },
                  };
                
                   chart2 = new Chart(document.getElementById('chart_Acc2'), config);
            }
            loadAccount2()
            // Populate Account3
            function loadAccount3(){
                const data = {
                    labels: acc_3_time.map(e => e),
                    datasets: [
                      {
                        label: 'Equity',
                        data: acc_3_equity.map(e => e),
                        borderColor: 'red',
                        fill: false,
                      },
                      {
                        label: 'Balance',
                        data: acc_3_balance.map(e => e),
                        borderColor: 'blue',
                        fill: false,
                      },
                    ],
                  };
                
                  let config = {
                    type: 'line',
                    data,
                    options: {
                      scales: {
                        x: {
                          title: {
                            display: true,
                            text: 'Time',
                          },
                        },
                        y: {
                          title: {
                            display: true,
                            text: 'Equity and Balance',
                          },
                        },
                      },
                    },
                  };
                
                   chart3 = new Chart(document.getElementById('chart_Acc3'), config);
                   
            }
            loadAccount3()
            },
            error:function(err){
    
            }
        })

    }
    // $(document).ready(function() {
        setInterval(function(){
          chart1.destroy()
          chart3.destroy()
          chart2.destroy();
          setTimeout(function() {
            fetchAccounts();
          }, 6000);
          // fetchAccounts()
          console.log("Hello bottom")},60000 )
        // fetchAccounts(); // call the function every minute (60,000 milliseconds)
        // console.log("Hello bottom")
    // });
    
})
