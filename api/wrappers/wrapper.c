#include "wrapper.h"

/*
output=pythonapi wrapper
*/
void set_pythonapi(struct ccx_s_options *api_options){
    api_add_param(api_options,"-pythonapi");
}

/*
autoprogram wrapper
*/
void setautoprogram(struct ccx_s_options *api_options){
    api_add_param(api_options,"-autoprogram");
}

/*
stdout wrapper
*/
void setstdout(struct ccx_s_options *api_options){
    api_add_param(api_options,"-stdout");
}

/*
pesheader wrapper
*/
void setpesheader(struct ccx_s_options *api_options){
    api_add_param(api_options,"-pesheader");
}

/*
debugdvbsub wrapper
*/
void setdebugdvbsub(struct ccx_s_options *api_options){
    api_add_param(api_options,"-debugdvbsub");
}

