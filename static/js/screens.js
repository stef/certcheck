
screens = {
	'Chrome': {
		'Default CA/cert': [
			{
				'src': 'certcheck_chromium_msauthority01.png',
				'label': 'Valid Certificate details'
			}
		],
		'Default CA, similar cert': [
			{
				'src': 'certcheck_chromium_mrsimillar01.png',
				'label': 'Similar Certificate details'
			}
		],
		'Similar CA, similar cert': [
			{
				'src': 'certcheck_chromium_simillarjunior01.png',
				'label': 'Valid Similar Certificate details'
			}
		],
		'Self-signed cert': [
			{
				'src': 'certcheck_chromium_drselfsigned01.png',
				'label': 'Chrome reaction'
			},{
				'src': 'certcheck_chromium_drselfsigned02.png',
				'label': 'Chrome reaction details'
			},{
				'src': 'certcheck_chromium_drselfsigned03.png',
				'label': 'Chrome URL bar reaction'
			},{
				'src': 'certcheck_chromium_drselfsigned04.png',
				'label': 'Certificate details'
			}
		],
		'Faked cert and CA': [
			{
				'src':'certcheck_chromium_unknownvalid01.png',
				'label': 'Chrome reaction'
			},{
				'src':'certcheck_chromium_unknownvalid02.png',
				'label': 'Chrome reaction details'
			},{
				'src':'certcheck_chromium_unknownvalid03.png',
				'label': 'Chrome URL bar reaction'
			},{
				'src':'certcheck_chromium_unknownvalid04.png',
				'label': 'Certificate details'
			}
		],
		'A valid but untrusted CA, real cert': [
			{
				'src': 'certcheck_chromium_jackmiddleattacer01.png',
				'label': 'Chrome reaction'
			},{
				'src': 'certcheck_chromium_jackmiddleattacer02.png',
				'label': 'Chrome reaction details'
			},{
				'src': 'certcheck_chromium_jackmiddleattacer03.png',
				'label': 'Chrome URL bar reaction'
			},{
				'src': 'certcheck_chromium_jackmiddleattacer04.png',
				'label': 'Certificate details'
			}
		]
	},
	'Firefox': {
		'Default CA/cert': [
			{
				'src':'d1.png',
				'label': 'Valid Certificate'
			}
		],
		'Default CA, similar cert': [
			{
				'src':'sm2.png',
				'label': 'Firefox reaction'
			},{
				'src':'d2.png',
				'label': 'Firefox add exception to Certificate'
			}
		],
		'Similar CA, similar cert': [
			{
				'src':'sm3.png',
				'label': 'Firefox reaction'
			},{
				'src':'d3.png',
				'label': 'Firefox add exception to Certificate'
			}
		],
		'Self-signed cert': [
			{
				'src':'sm4.png',
				'label': 'Firefox reaction'
			},{
				'src':'d4.png',
				'label': 'Firefox add exception to Certificate'
			}
		],
		'Faked cert and CA': [
			{
				'src':'sm5.png',
				'label': 'Firefox reaction'
			},{
				'src':'d5.png',
				'label': 'Firefox add exception to Certificate'
			}
		],
		'A valid but untrusted CA, real cert': [
			{
				'src':'sm6.png',
				'label': 'Firefox reaction'
			},{
				'src':'d6.png',
				'label': 'Firefox add exception to Certificate'
			}		
		]
	}
}