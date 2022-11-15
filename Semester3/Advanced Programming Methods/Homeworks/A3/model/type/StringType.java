package model.type;

import model.value.StringValue;
import model.value.Value;

public class StringType implements Type{
    @Override
    public boolean equals(Type anotherType){
        return anotherType instanceof StringType;
    }

    @Override
    public Value defaultValue() {
        return new StringValue("");
    }

    public String toString(){
        return "string";
    }
}
