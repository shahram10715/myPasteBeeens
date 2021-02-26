" source $VIMRUNTIME/defaults.vim

set nocp
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

set nocompatible
set path+=**

highlight clear
if exists("syntax_on")
    syntax reset
endif

let colors_name = "comments"

" First set Normal to regular white on black text colors:
hi Normal ctermfg=LightGray ctermbg=Black guifg=#dddddd	guibg=Black

" Syntax highlighting (other color-groups using default, see :help group-name):
hi Comment    cterm=NONE ctermfg=Red
hi Constant   cterm=NONE ctermfg=White
hi Identifier cterm=NONE ctermfg=White
hi Function   cterm=NONE ctermfg=White
hi Statement  cterm=NONE ctermfg=White
hi PreProc    cterm=NONE ctermfg=White
hi Type	      cterm=NONE ctermfg=White
hi Special    cterm=NONE ctermfg=White
hi Delimiter  cterm=NONE ctermfg=White
