package model.type;

import model.value.IntValue;
import model.value.Value;

public class IntType implements Type{
    @Override
    public boolean equals(Object another) {
        if(another instanceof IntType)
            return true;
        else
            return false;
    }

    @Override
    public String toString(){
        return "int";
    }

    @Override
    public Value defaultValue() {
        return new IntValue(0);
    }

}
