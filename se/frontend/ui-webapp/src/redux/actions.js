// Define actions
export const LOGIN_USER_SUCCESS = 'LOGIN_USER_SUCCESS';
export const LOGIN_USER_FAILURE = 'LOGIN_USER_FAILURE';
export const LOGIN_USER_REQUEST = 'LOGIN_USER_REQUEST';
export const LOGOUT_USER = 'LOGOUT_USER';

export const REGISTER_USER_SUCCESS = 'REGISTER_USER_SUCCESS';
export const REGISTER_USER_FAILURE = 'REGISTER_USER_FAILURE';
export const REGISTER_USER_REQUEST = 'REGISTER_USER_REQUEST';

export const FETCH_PROTECTED_DATA_REQUEST = 'FETCH_PROTECTED_DATA_REQUEST';
export const RECEIVE_PROTECTED_DATA = 'RECEIVE_PROTECTED_DATA';


// Action Creators
export function uploadImage(images) {
    return {type: UPLOAD_IMAGE, images: images}
}

export function deleteImage(id) {
    return {type: DELETE_IMAGE, id: id}
}
