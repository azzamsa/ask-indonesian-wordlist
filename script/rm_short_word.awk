{
    if( $1 ~ /[a-z]|[A-Z]|[a-z]{2}|[A-Z]{2}/){ # remove short word
        next;
    }
    print $0;
}
