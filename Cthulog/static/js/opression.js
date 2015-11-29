/*
 * requires md5.min.js from https://github.com/blueimp/JavaScript-MD5
 *
 * Accept
 * 		message(str)
 * 		difficulty(str)
 * 		disemvowelling_threshold(int)
 * Return
 *		results(object)
 *		{
 * 			"message": str,
 * 			"randint": int,
 * 			"the_hash": str
 * 		}
 * 	
 * if difficulty length is >= threshold, message will have all vowells removed,
 * thus increasing annoyance and pretending not to censor with a thumb firmly
 * planted in one's rectum.
 */
function helpHesOpressingMe (difficulty) {

	// generate random 10-digit number
	var randint = parseInt(Math.random() * 0xFFFFFFFF);
	var leading_zeroes = new RegExp("^" + difficulty);

	// here is where the goodies go back to the server, yo.
	function send_message(results) {
		console.log(results);
	}

	// recursively search for a hash that matches our critera
	function hassledByTheMan(randint, count, leading_zeroes) {
		var the_hash = md5(randint.toString());
		if (the_hash.match(leading_zeroes)) {
			send_message({
				"randint": randint,
				"the_hash": the_hash
			});
			return;
		}

		randint += 1;
		count += 1;
		// javascript needs a breather every now and then to 
		// flush the cache. Don't hate.
		if (count >= 1000) {
			setTimeout(function () {
				count = 0;
				hassledByTheMan(randint, count, leading_zeroes);
			}, 25);
		} else {
			hassledByTheMan(randint, count, leading_zeroes);
		}
	}
	hassledByTheMan(randint, 0, leading_zeroes);
}

$("#post_message").on("click", function () {
	var  = $("#message").text();
	$.ajax({
		url: "opression/supplicant",
		method: "POST",
		type: "JSON",
		data: JSON.stringify({
			"messsage_id"
		})
	})
	.success(function (data) {
		// set sesson cookie from data
		helpHesOpressingMe(data.difficulty);
	})
	.failure(function (error) {
		console.log("handle the fail");
	});
});
//var message = "I vociferously support Trump for president 2015! WAKE UP, SHEEPLE!!!1";
//var difficulty = "000000";


//TODO set session cookie
