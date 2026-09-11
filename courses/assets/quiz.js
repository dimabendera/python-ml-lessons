(function(){
  var done=0, right=0;
  document.querySelectorAll('.q').forEach(function(q){
    var ok=+q.dataset.ok, answered=false;
    q.querySelectorAll('.opt').forEach(function(btn){
      btn.addEventListener('click', function(){
        if(answered) return;
        answered=true; done++;
        var pick=+btn.dataset.i;
        if(pick===ok) right++;
        q.querySelectorAll('.opt').forEach(function(b){
          var i=+b.dataset.i;
          b.disabled=true;
          if(i===ok) b.classList.add('right');
          else if(i===pick) b.classList.add('wrong');
        });
        q.querySelector('.why').classList.add('show');
        document.getElementById('done').textContent=done;
        document.getElementById('right').textContent=right;
      });
    });
  });
})();
