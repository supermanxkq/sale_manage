/**
 * Created by xukaiqiang on 2019/6/23.
 */
/**
   * 反序列化JSON对象到form
   */
   var deserializeObject = function(obj) {
    obj = $.extend({}, obj);

    //
    //对象扁平化
    //
    this.map(function() {
      var elements = $.prop(this, "elements");
      return elements ? $.makeArray(elements) : this;
    }).each(function() {
      var n = this.name;
      if(n && n.indexOf('.') != -1 && !obj.hasOwnProperty(n)) {
        obj[n] = app.getNestedProperty(n, obj);
      }
    });

    $(this).deserialize(obj, {
      //
      //反序列化每一form元素时的回调
      //
      change: function(value) {
        var elem = $(this);
        if(elem.is('.jstreeselect-hidden-input')) {
          elem.jstreeVal(value);
        } else if(elem.is('.jstreemultiselect-hidden-input')) {
          elem.jstreemultiVal(value);
        } else if(elem.is('.select2-hidden-accessible > option')) {
          elem.val(value).trigger("change");
        } else if(elem.is('[data-selectloader-store] > option')) {
          elem.val(value).trigger("change");
        } else if(elem.is('[data-radioloader-name] input[type="radio"]')) {
          elem.val(value).trigger("change");
        } else if(elem.is('[data-checkboxloader-name] input[type="checkbox"]')) {
          elem.val(value).trigger("change");
          /*ln 文本框显示 回显*/
        } else if(elem.is('textarea')) {
          elem.val(value);
        }
      }
    });
  };
