source $VIMRUNTIME/defaults.vim

set number
set tabstop=4
set shiftwidth=4
set expandtab
set completeopt-=preview

inoremap " ""<left>
inoremap ' ''<left>
inoremap ( ()<left>
inoremap [ []<left>
inoremap { {}<left>

call plug#begin()
Plug 'mattn/emmet-vim'
Plug 'JuliaEditorSupport/julia-vim'
call plug#end()
