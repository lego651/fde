/* FDE PIN gate. Loaded in <head> of every page of a PIN-protected client:
 *   <script src="/fde/assets/pin-gate.js" data-client="kidsmap" data-hash="<sha256 of 'kidsmap:PIN'>"></script>
 * Hides the page until the right 4-digit PIN is entered, then remembers it on this device.
 * This is a privacy screen for casual visitors, not real security: the site and repo are public. */
(function () {
  var me = document.currentScript;
  var client = me.getAttribute('data-client');
  var hash = me.getAttribute('data-hash');
  var KEY = 'fde-pin:' + client;
  var root = document.documentElement;
  try { if (localStorage.getItem(KEY) === hash) return; } catch (e) {}

  root.classList.add('pin-locked');
  var css = document.createElement('style');
  css.textContent =
    'html.pin-locked body{visibility:hidden}' +
    '#pin-gate{visibility:visible;position:fixed;inset:0;z-index:2147483647;display:grid;place-items:center;background:#fbf8f2;font:400 16px/1.5 "Archivo","Noto Sans SC",system-ui,sans-serif;color:#2a2620}' +
    '#pin-gate form{display:grid;gap:14px;justify-items:center;background:#fff;border:1px solid #ebe3d4;border-radius:18px;padding:28px 30px;box-shadow:0 10px 30px rgba(60,40,10,.08);width:min(320px,90vw)}' +
    '#pin-gate h1{margin:0;font-size:1.25rem}' +
    '#pin-gate p{margin:0;color:#6d6558;font-size:.9rem;text-align:center}' +
    '#pin-gate input{width:100%;font:700 1.8rem/1 ui-monospace,Menlo,monospace;letter-spacing:.6em;text-align:center;padding:10px 0 10px .6em;border:2px solid #d9cfbd;border-radius:12px;background:#fdfbf7;color:#2a2620}' +
    '#pin-gate input:focus{outline:none;border-color:#c9772e}' +
    '#pin-gate button{width:100%;font:700 1rem "Archivo",system-ui,sans-serif;background:#2a2620;color:#fff;border:0;border-radius:12px;padding:11px;cursor:pointer}' +
    '#pin-gate button:focus-visible{outline:3px solid #c9772e;outline-offset:2px}' +
    '#pin-gate .err{color:#b3261e;font-weight:700;min-height:1.2em}' +
    '#pin-gate form.shake{animation:pinshake .3s}' +
    '@keyframes pinshake{25%{transform:translateX(-8px)}75%{transform:translateX(8px)}}' +
    '@media (prefers-reduced-motion:reduce){#pin-gate form.shake{animation:none}}';
  document.head.appendChild(css);

  function sha256(text) {
    return crypto.subtle.digest('SHA-256', new TextEncoder().encode(text)).then(function (buf) {
      return Array.prototype.map.call(new Uint8Array(buf), function (b) { return ('0' + b.toString(16)).slice(-2); }).join('');
    });
  }

  function show() {
    var gate = document.createElement('div');
    gate.id = 'pin-gate';
    gate.setAttribute('role', 'dialog');
    gate.setAttribute('aria-modal', 'true');
    gate.setAttribute('aria-labelledby', 'pin-gate-h');
    gate.innerHTML =
      '<form novalidate>' +
      '<h1 id="pin-gate-h">请输入 PIN</h1>' +
      '<p>这个项目需要 4 位 PIN 才能查看</p>' +
      '<label for="pin-gate-in" style="position:absolute;left:-9999px">PIN</label>' +
      '<input id="pin-gate-in" type="password" inputmode="numeric" autocomplete="off" maxlength="4" pattern="[0-9]*" aria-describedby="pin-gate-err">' +
      '<span class="err" id="pin-gate-err" aria-live="polite"></span>' +
      '<button type="submit">打开</button>' +
      '</form>';
    document.body.appendChild(gate);
    var form = gate.querySelector('form'), input = gate.querySelector('input'), err = gate.querySelector('.err');
    input.focus();
    function tryPin() {
      var pin = input.value.replace(/\D/g, '');
      if (pin.length !== 4) { err.textContent = '请输入 4 位数字'; return; }
      sha256(client + ':' + pin).then(function (h) {
        if (h === hash) {
          try { localStorage.setItem(KEY, hash); } catch (e) {}
          gate.remove();
          root.classList.remove('pin-locked');
        } else {
          err.textContent = 'PIN 不对，请再试一次';
          input.value = '';
          form.classList.remove('shake'); void form.offsetWidth; form.classList.add('shake');
          input.focus();
        }
      });
    }
    form.addEventListener('submit', function (ev) { ev.preventDefault(); tryPin(); });
    input.addEventListener('input', function () { err.textContent = ''; if (input.value.replace(/\D/g, '').length === 4) tryPin(); });
  }

  if (document.body) show(); else document.addEventListener('DOMContentLoaded', show);
})();
