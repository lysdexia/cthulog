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
function helpHesOpressingMe (message, difficulty, disemvowelling_threshold) {

	// generate random 10-digit number
	var randint = parseInt(Math.random() * 0xFFFFFFFF);
	var leading_zeroes = new RegExp("^" + difficulty);

	// if you are really in the shit, shaddap
	function disemVowell(s) {
		return s.replace(/[aeiou]+/gi, "");
	}

	// here is where the goodies go back to the server, yo.
	function send_message(results) {
		if (difficulty.length >= disemvowelling_threshold) {
			message = disemVowell(message);
		}
		results.message = message;
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
		// flush the cache. Don't hate. That's my job.
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

var disemvowelling_threshold = 6;
var message = "I vociferously support Trump for president 2016! WAKE UP, SHEEPLE!!!1";
var difficulty = "000000";

helpHesOpressingMe(message, difficulty, disemvowelling_threshold);

