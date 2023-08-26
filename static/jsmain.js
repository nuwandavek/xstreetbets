$(".market-row").click(function(){
    var market_id = $(this).attr("data-market");
    window.location.href = "/market/" + market_id;
});