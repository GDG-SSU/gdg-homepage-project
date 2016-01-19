/**
 * Created by Genus on 2016. 1. 14..
 */
/**
 * Copyright (c) 2011, 2014 Juho Nurminen
 *
 * This software is provided 'as-is', without any express or implied
 * warranty. In no event will the authors be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 *    1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 *
 *    2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 *
 *    3. This notice may not be removed or altered from any source
 *    distribution.
 */

(function () {

    var i, j, script,
        open = XMLHttpRequest.prototype.open,
        setRequestHeader = XMLHttpRequest.prototype.setRequestHeader,
        send = XMLHttpRequest.prototype.send,
        submit = HTMLFormElement.prototype.submit,
        button,
        formCatcher,

        // boudary creator for multipart/form-data
        getBoundary = function (data) {
                var i,
                    chars = '0123456789AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
                    boundary = '----WebKitFormBoundary';

                for (i = 0; i < 16; i++) {
                    boundary += chars[Math.floor(Math.random()*62)];
                }

                for (i = 0; i < data.length; i++) {
                    if (data[i][0].match(boundary) || data[i][1].match(boundary)) {
                        boundary = getBoundary(data);
                        break;
                    }
                }

                return boundary;
            },

        array = function () { // JSON fix
                var a = window.Array.apply(window, arguments);
                a.toJSON = undefined;
                return a;
            },

        serializeForm = function (form) {
                var url = form.getAttribute('action') || '',
                    method = form.getAttribute('method') && form.getAttribute('method').toUpperCase() == 'POST' ? 'POST' : 'GET',
                    data = array(),
                    multipart = form.getAttribute('enctype') &&
                                form.getAttribute('enctype').substr(0, 19).toLowerCase() == 'multipart/form-data'
                                ? true : false;

                // parse the data
                for (i = 0; i < form.length; i++) {
                    if (form[i].name && form[i].getAttribute('disabled') === null) {
                        if (multipart && method == 'POST' && form[i].nodeName == 'INPUT' && form[i].type.toUpperCase() == 'FILE' && form[i].files.length) {
                            for (j = 0; j < form[i].files.length; j++) {
                                data.push(
                                        'Content-Disposition: form-data; name="' + encodeURIComponent(form[i].name) + '"; ' +
                                            'filename="' + encodeURIComponent(form[i].files[j].name) + '"\n' +
                                        'Content-Type: ' + (form[i].files[j].type || 'text/plain') + '\n\n' +
                                        '[File contents not captured]'
                                    );
                            }
                        } else if (
                                (form[i].nodeName == 'INPUT' &&
                                    (form[i].type.toUpperCase() == 'RADIO' || form[i].type.toUpperCase() == 'CHECKBOX' ? form[i].checked : true) &&
                                    (form[i].type.toUpperCase() == 'SUBMIT' ? form[i].isSameNode(button) : true)) ||
                                form[i].nodeName == 'SELECT' ||
                                form[i].nodeName == 'BUTTON' ||
                                form[i].nodeName == 'TEXTAREA'
                            ) {
                            data.push(array(form[i].name, form[i].value));
                        }
                    }
                }

                // append GET data to the URL
                if (method == 'GET') {
                    if (url.indexOf('#') != -1) {
                        url = url.substr(0, url.indexOf('#'));
                    }
                    if (url.indexOf('?') != -1 && url.charAt(url.length-1) != '&') {
                        url += '&';
                    } else {
                        url += '?';
                    }

                    for (i = 0; i < data.length; i++) {
                        url += (i ? '&' : '' ) + encodeURIComponent(data[i][0]) + '=' + encodeURIComponent(data[i][1]);
                    }

                    data = array(); // clear data
                }

                return {
                    'type': 'Form',
                    'method': method,
                    'url': url,
                    'headers': method == 'POST' ? array(array(
                            'Content-Type',
                            multipart ? 'multipart/form-data; boundary=' + getBoundary(data) : 'application/x-www-form-urlencoded'
                        )) : array(),
                    'data': data
                };
            };

    // get this script element
    for (i = 0; i < document.scripts.length; i++) {
        if (document.scripts[i].src == 'chrome-extension://kajfghlhfkcocafkcjlajldicbikpgnp/catcher.js' ||
            (document.scripts[i].src == 'chrome-extension://hghmdhgjmjbilodfdaabijjjncdggnob/catcher.js')) {
            script = document.scripts[i];
        }
    }
    if (!script) {
        return;
    }

    // clean up on node remove
    document.documentElement.addEventListener('DOMNodeRemoved', function (event) {
            if (event.target.isSameNode(script)) {
                XMLHttpRequest.prototype.open = open;
                XMLHttpRequest.prototype.setRequestHeader = setRequestHeader;
                XMLHttpRequest.prototype.send = send;
                window.removeEventListener('submit', formCatcher, true);
                HTMLFormElement.prototype.submit = submit;
                document.documentElement.removeEventListener('DOMNodeRemoved', arguments.callee);
            }
        });

    // Catch XHR
    XMLHttpRequest.prototype.open = function (method, url) {
            open.apply(this, arguments);

            this['kajfghlhfkcocafkcjlajldicbikpgnp'] = {
                'type': 'XHR',
                'method': method.toUpperCase(),
                'url': url.toString()
            };
        };

    XMLHttpRequest.prototype.setRequestHeader = function (header, value) {
            setRequestHeader.apply(this, arguments);

            header = header === null || header === undefined ? header : header.toString();
            value = value === null || value === undefined ? value : value.toString();

            if (!('headers' in this['kajfghlhfkcocafkcjlajldicbikpgnp'])) {
                this['kajfghlhfkcocafkcjlajldicbikpgnp'].headers = array();
            }

            if (!( // Check for 'unsafe' headers
                    header.match(/^Accept-Charset$/i) ||
                    header.match(/^Accept-Encoding$/i) ||
                    header.match(/^Connection$/i) ||
                    header.match(/^Content-Length$/i) ||
                    header.match(/^Cookie$/i) ||
                    header.match(/^Cookie2$/i) ||
                    header.match(/^Content-Transfer-Encoding$/i) ||
                    header.match(/^Date$/i) ||
                    header.match(/^Expect$/i) ||
                    header.match(/^Host$/i) ||
                    header.match(/^Keep-Alive$/i) ||
                    header.match(/^Referer$/i) ||
                    header.match(/^TE$/i) ||
                    header.match(/^Trailer$/i) ||
                    header.match(/^Transfer-Encoding$/i) ||
                    header.match(/^Upgrade$/i) ||
                    header.match(/^User-Agent$/i) ||
                    header.match(/^Via$/i) ||
                    header.match(/^Proxy-/i) ||
                    header.match(/^Sec-/i) ||
                    header.match(/^Origin$/i)
                )) {
                this['kajfghlhfkcocafkcjlajldicbikpgnp'].headers.push(array(header, value));
            }
        };

    XMLHttpRequest.prototype.send = function (data) {
            var event = document.createEvent('CustomEvent');

            send.apply(this, arguments);

            if (data === null || data === undefined) {
                this['kajfghlhfkcocafkcjlajldicbikpgnp'].data = array();
            } else if (data instanceof FormData) {
                this['kajfghlhfkcocafkcjlajldicbikpgnp'].data = array('[Unable to capture XHR Level 2 FormData]');
            } else {
                this['kajfghlhfkcocafkcjlajldicbikpgnp'].data = array(data.toString());
            }

            event.initCustomEvent('kajfghlhfkcocafkcjlajldicbikpgnp', false, false, this['kajfghlhfkcocafkcjlajldicbikpgnp']);
            script.dispatchEvent(event);
            delete this['kajfghlhfkcocafkcjlajldicbikpgnp'];
        };

    // Catch form submissions
    window.addEventListener('click', function (event) {
            if (
                    (event.target.nodeName == 'INPUT' && event.target.type && event.target.type.toUpperCase() == 'SUBMIT') ||
                    (event.target.nodeName == 'BUTTON' && (!event.target.type || (event.target.type.toUpperCase() != 'BUTTON' && event.target.type.toUpperCase() != 'RESET')))
                ) {
                // remember a click on a submit button
                button = event.target;
                // queue an asychronous function
                setTimeout(function () {
                        // forget the click
                        delete button;
                    }, 0);
            }
        }, true);

    window.addEventListener('submit', formCatcher = function (event) {
            var result = document.createEvent('CustomEvent');

            result.initCustomEvent('kajfghlhfkcocafkcjlajldicbikpgnp', false, false, serializeForm(event.target));
            script.dispatchEvent(result);
        }, true);

    HTMLFormElement.prototype.submit = function () {
            submit.apply(this, arguments);
            formCatcher({'target': this});
        };

})();
