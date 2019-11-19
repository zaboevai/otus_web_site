{
    subscribe.onclick = function () {
        if (form.userFields.hidden == true) {
            form.userFields.hidden = false;
        } else {
            form.userFields.hidden = true;
        }
    }
    SubscribeButton.onclick = function () {
//    object_list.SubscribeEmail
        form.userFields.hidden = true;
    }
}