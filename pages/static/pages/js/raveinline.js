const API_publicKey = "FLWPUBK_TEST-f7781a09cfbfdc809b69aa6f67ed21fa-X";

    	function payWithRave() {
        	var x = getpaidSetup({
            	PBFPubKey: API_publicKey,
            	customer_email: "user@example.com",
            	amount: 2000,
            	currency: "NGN",
            	txref: "rave-123456",
            	subaccounts: [
              	{
                	id: "RS_CF15E38FBC5CECEFD594D463A36E51AE" // This assumes you have setup your commission on the dashboard.
              	}
            	],
            	meta: [{
                	metaname: "flightID",
                	metavalue: "AP1234"
            	}],
            	onclose: function() {},
            	callback: function(response) {
                	var txref = response.tx.txRef; // collect flwRef returned and pass to a 					server page to complete status check.
                	console.log("This is the response returned after a charge", response);
                	if (
                    	response.tx.chargeResponseCode == "00" ||
                    	response.tx.chargeResponseCode == "0"
                	) {
                    	// redirect to a success page
                    	window.location = "successpage/";
                	} else {
                    	// redirect to a failure page.
                    	window.location = "errorpage/";
                	}

                	x.close(); // use this to close the modal immediately after payment.
            	}
        	});
    	}