

function saveTrade(object_id){
	$("#error_box").html("");
	
	var trade_type = $("#trade_type option:selected").text();
	var stock_symbol = $("#stock_symbol").val();
	var number_of_shares = $("#number_of_shares").val();
	
	console.log(trade_type);
	$.post(
		"/api/trade", 
		{ 
			trade_type: trade_type,
			stock_symbol: stock_symbol,
			number_of_shares: number_of_shares
		},
	   	function(p) {
	   		if (p.error){
	   			$("#error_box").html(p.error);
	   		}
	   		if (p.status){
	   			var h = "";
	   			h += p.status;
	   			h += p.transaction.data;
	 			$("#error_box").html(h);  			
		   		$("#stock_symbol").val("");
		   		$("#number_of_shares").val("");
	   		}
	   		console.log(p);
	   		

	   	}
	);
};

function getPortfolio(portfolio_id, prices){
	    var url = "/api/portfolio/";
		url += portfolio_id;
		if (prices == true){
			url += "?prices=true"
		}
		console.log(url);
		
		$.ajax({
		    url: url,
		    type: 'GET',
		    success: function(data){ 
			   	console.log(data);
			   	portfolio_value = 0;
			   	var h = "";
			   	var positions = $.parseJSON(data.positions);
			   	h += "<table class='portfolio_table'>";
			   	h += "<thead>";
			   	h += "<th>" + "stock" + "</th>";
			   	h += "<th>" + "quantity" + "</th>";
			   	h += "<th>" + "current price" + "</th>";
			   	h += "<th>" + "value" + "</th>";
			   	h += "</thead>";
			   	var i = 0;
			   	$.each(positions, function(key,val){
				   	if (i%2 == 0){
			   			h += "<tr>";
				   	}
			   		else{
			   			h += "<tr class='odd'>";	
			   		}
			   		h += "<td><a href='/stock/" + key + "'>" + key + "</td>";
			   		h += "<td>" + val.shares + "</td>";
			   		
			   		if (val.price){
			   			h += "<td>" + val.price + "</td>";
			   		}
			   		else{
			   			h += "<td>" + "loading.." + "</td>";
			   		}
			   		h += "<td>" + (val.shares * val.price).formatMoney(2,',','.'); + "</td>";
					portfolio_value += (val.shares * val.price);
			   		h += "</tr>";
			   		i = i + 1;
				});
				h += "</table>";
								
			   	$("#porfolio").html(h);
			   	
			   	

			   	
			   	//Build Balance
			   	var j = "";
			   	j += "<table class='balance_table'>";
			   	j += "<thead>";
			   	j += "<th>" + "Cash Balance" + "</th>";
			   	j += "</thead>";
			   	j += "<tr><td>$ " + data.balance.formatMoney(2,',','.'); + "</td></tr>";
			   	j += "</table>";
			   	portfolio_value += data.balance;
			   	$("#balance").html(j);


			   	//Build Portfolio Value
			   	var j = "";
			   	j += "<table class='balance_table'>";
			   	j += "<thead>";
			   	j += "<th>" + "Portfolio Value" + "</th>";
			   	j += "</thead>";
			   	console.log(portfolio_value);
			   	j += "<tr><td>$ " + portfolio_value.formatMoney(2,',','.'); + "</td></tr>";
			   	j += "</table>";
			   	$("#portfolio_value").html(j);

			}
		});
}


Number.prototype.formatMoney = function(decPlaces, thouSeparator, decSeparator) {
    var n = this,
    decPlaces = isNaN(decPlaces = Math.abs(decPlaces)) ? 2 : decPlaces,
    decSeparator = decSeparator == undefined ? "." : decSeparator,
    thouSeparator = thouSeparator == undefined ? "," : thouSeparator,
    sign = n < 0 ? "-" : "",
    i = parseInt(n = Math.abs(+n || 0).toFixed(decPlaces)) + "",
    j = (j = i.length) > 3 ? j % 3 : 0;
    return sign + (j ? i.substr(0, j) + thouSeparator : "") + i.substr(j).replace(/(\d{3})(?=\d)/g, "$1" + thouSeparator) + (decPlaces ? decSeparator + Math.abs(n - i).toFixed(decPlaces).slice(2) : "");
};
