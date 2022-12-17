package model.value;

import model.type.IntType;
import model.type.Type;

public class IntValue implements Value{
    private final int val;

    public IntValue(int v){
        val = v;
    }

    public int getVal(){
        return this.val;
    }

    @Override
    public Type getType() {
        return new IntType();
    }

    @Override
    public String toString(){
        return String.format("%d", this.val);
    }


}
